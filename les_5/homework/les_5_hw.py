from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import uvicorn as uvicorn
from random import randint




app = FastAPI()


tasks = []

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: str

class TaskIn(BaseModel):
    title: str
    description: Optional[str] = None
    status: str


@app.get("/tasks/", response_model=list[Task])
async def root():
    return tasks

@app.post("/tasks/", response_model=list[Task])
async def create_task(new_task: TaskIn):
    tasks.append(Task(id=len(tasks) + 1), title=new_task.title, description=new_task.description, status=new_task.status)
    return tasks

@app.put("/tasks/", response_model=Task)
async def edit_task(task_id: int, new_task: TaskIn):
    cur_task = None
    for i in range(0, len(tasks)):
        if tasks[i].id == task_id:
            cur_task = tasks[task_id - 1]
    if cur_task:
        cur_task.title = new_task.title
        cur_task.description = new_task.description
        cur_task.status = new_task.status
    else:
        raise HTTPException(status_code=404, detail='Task not found')
    return cur_task


@app.delete("/tasks/", response_model=dict)
async def delete_task(task_id: int):
    for i in range(0, len(tasks)):
        if tasks[i].id == task_id:
            tasks.remove(tasks[i])
            return {'message': 'Task was deleted'}
    raise HTTPException(status_code=404, detail='Task not found')
    







if __name__ == '__main__':
    uvicorn.run('les_5_hw:app', host='127.0.0.1', port=8000, reload=True)