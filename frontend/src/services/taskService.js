import { apiRequest } from "./api";

const TASKS_ENDPOINT = "/tasks/";

// GET: Fetch all tasks
export function getTasks() {
    return apiRequest(TASKS_ENDPOINT);
}

// GET: Fetch a particular task
export function getTaskById(taskId) {
    return apiRequest(`${TASKS_ENDPOINT}${taskId}`);
}

// POST: Create a new task
export function createTask(taskData) {
    return apiRequest(TASKS_ENDPOINT, {
        method: "POST",
        body: JSON.stringify(taskData),
    });
}

// PATCH: Update an existing task
export function updateTask(taskId, taskData) {
    return apiRequest(`${TASKS_ENDPOINT}${taskId}`, {
        method: "PATCH",
        body: JSON.stringify(taskData),
    });
}

// DELETE: Delete a task
export function deleteTask(taskId) {
    return apiRequest(`${TASKS_ENDPOINT}${taskId}`, {
        method: "DELETE",
    });
}