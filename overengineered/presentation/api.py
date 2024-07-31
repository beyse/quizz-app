from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from application.quiz_service import QuizService

app = FastAPI()

class AnswerSubmission(BaseModel):
    answer_index: int

class QuizService:
    # ... (implementation details)

quiz_service = QuizService(...)  # Initialize with proper dependencies

@app.post("/start_quiz")
async def start_quiz():
    quiz_service.start_quiz()
    return {"message": "Quiz started"}

@app.get("/next_question")
async def get_next_question():
    question = quiz_service.get_next_question()
    return {
        "question_text": question.get_text(),
        "answers": [answer.text for answer in question.get_answers()]
    }

@app.post("/submit_answer")
async def submit_answer(submission: AnswerSubmission):
    is_correct = quiz_service.submit_answer(submission.answer_index)
    return {"is_correct": is_correct}

@app.post("/end_quiz")
async def end_quiz():
    result = quiz_service.end_quiz()
    return {
        "correct_answers": result.correct_answers,
        "total_questions": result.total_questions,
        "duration": result.duration
    }