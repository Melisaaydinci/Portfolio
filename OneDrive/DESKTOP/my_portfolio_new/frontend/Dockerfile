# Node imajını kullan
FROM node:16-alpine

# Çalışma dizinini belirle
WORKDIR /frontend

# Paket dosyalarını kopyala ve bağımlılıkları yükle
COPY package.json package-lock.json ./
RUN npm install

# Uygulama dosyalarını kopyala
COPY . /frontend/

# React uygulamasını Vite ile geliştirme sunucusu ile çalıştır
CMD ["npm", "run", "dev"]
