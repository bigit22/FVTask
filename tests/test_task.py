import pytest

@pytest.mark.asyncio
async def test_create_and_get_task(async_client):
    response = await async_client.post("/tasks/", json={
        "title": "Test Task",
        "description": "Test Description",
        "status": "pending"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["status"] == "pending"
    task_id = data["id"]

    response = await async_client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["description"] == "Test Description"

@pytest.mark.asyncio
async def test_list_tasks(async_client):
    response = await async_client.get("/tasks/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
