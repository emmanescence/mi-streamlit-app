import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Configuración de la página
st.set_page_config(layout="wide", page_title="Evolución del Precio de la Acción")

# Título de la aplicación
st.title("Evolución del Precio de la Acción y su Media Móvil")

# Selección de la acción
ticker = st.text_input("Ingrese el ticker de la acción (por ejemplo, AAPL):", "AAPL")

# Selección del rango de fechas
start_date = st.date_input("Fecha de inicio:", pd.to_datetime("2023-01-01"))
end_date = st.date_input("Fecha de fin:", pd.to_datetime("2023-12-31"))

# Descarga de datos
if ticker:
    df = yf.download(ticker, start=start_date, end=end_date)
    
    # Cálculo de la media móvil
    df['SMA'] = df['Close'].rolling(window=20).mean()

    # Gráfico
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df.index, df['Close'], label=f"{ticker} Precio de Cierre", color='blue', linewidth=2)
    ax.plot(df.index, df['SMA'], label="Media Móvil (20 días)", color='orange', linestyle='--', linewidth=2)
    ax.set_title(f"Evolución del Precio de {ticker}", fontsize=16)
    ax.set_xlabel("Fecha", fontsize=12)
    ax.set_ylabel("Precio de Cierre (USD)", fontsize=12)
    ax.grid(True)
    ax.legend()
    
    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)
