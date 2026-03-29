FROM node:20-slim
WORKDIR /app
COPY server/package.json server/
RUN cd server && npm install
COPY server/ server/
COPY setup-wizard/ setup-wizard/
EXPOSE 3000
CMD ["node", "server/index.js"]
