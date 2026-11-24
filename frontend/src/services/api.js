const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000";

export async function apiRequest(endpoint, options = {}) {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
        ...options,
        headers: {
            "Content-Type": "application/json",
            ...options.headers,
        },
    });
    
    if(!response.ok){
        const errorData = await response.json().catch(() => null);

        const message = 
        errorData?.detail || "Something went wrong with the API request.";

        throw new Error(
            typeof message === "string"
            ? message
            :JSON.stringify(message)
        );
    }

    return response.json();
}