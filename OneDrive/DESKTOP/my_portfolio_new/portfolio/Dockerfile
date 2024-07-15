# Resmi Python imajını kullan
FROM python:3.10.6

# Çalışma dizinini belirle
WORKDIR /portfolio

# Gereksinim dosyasını kopyala ve bağımlılıkları yükle
COPY requirements.txt /portfolio/
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını kopyala
COPY . /portfolio/

# Ortam değişkenlerini ayarla
ENV DJANGO_SETTINGS_MODULE=portfolio.settings
ENV PYTHONUNBUFFERED=1

# Django uygulamasını geliştirme sunucusu ile çalıştır
CMD ["python", "portfolio/manage.py", "runserver", "0.0.0.0:8000"]
