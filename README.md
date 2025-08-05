# FeelTrack 🎯

FeelTrack is a FastAPI-based web application that analyzes comments or sentences scraped from websites and determines their sentiment (positive, negative, or neutral) using AI.

It leverages **HuggingFace Transformers** with pretrained sentiment analysis models and stores data in a **PostgreSQL** database via **SQLAlchemy**. The entire app is fully **Dockerized**.

---

## 🚀 Features

- 🔍 Real-time sentiment analysis using Hugging Face `transformers`
- 🧠 AI-powered comment processing
- 📊 PostgreSQL database integration
- 📦 Docker and Docker Compose setup
- 🔐 Environment variable management with `.env`
- 🌐 Interactive API docs with Swagger (`/docs`)

---

## 📁 Project Structure

```
feeltrack/
├── app/
│   ├── main.py
│   ├── core/
│   ├── models/
│   ├── crud/
│   ├── routes/
│   └── utils/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .env
```

---

## ⚙️ Setup

### 1. Clone the Repo

```bash
git clone https://github.com/amiradmin/FeelTrack.git
cd feeltrack
```

### 2. Add Environment Variables

Create a `.env` file at the project root:

```env
DATABASE_URL=postgresql://myuser:mypassword@db:5432/mydatabase
SECRET_KEY=supersecretkey
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 3. Build and Run with Docker

```bash
docker-compose up --build
```

This will:

- Build the FastAPI app
- Start the PostgreSQL database
- Expose the app on `http://localhost:8000`

---

## 🌐 API Docs

Once running, go to:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🧪 Example Usage

To analyze a sentence:

```http
POST /analyze

Request body:
{
  "text": "This product is amazing!"
}
```

Response:

```json
{
  "label": "POSITIVE",
  "score": 0.999
}
```

---

## 🐳 Docker Tips

- Rebuild image if you change dependencies:

  ```bash
  docker-compose down
  docker-compose up --build
  ```

- View logs:

  ```bash
  docker-compose logs -f
  ```

---

## 📌 TODO

- [ ] Web scraping integration
- [ ] Store analysis history in the DB
- [ ] Add user authentication
- [ ] Deploy to cloud (e.g., Render, Heroku, or Fly.io)

---

## 📃 License

MIT License. Free to use, share, and modify.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you’d like to change.


.