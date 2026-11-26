const API = import.meta.env.VITE_API_URL || "http://localhost:8000";

async function refreshToken() {
  const refresh_token = localStorage.getItem("refresh_token");
  if (!refresh_token) throw new Error("No refresh token");
  
  const res = await fetch(`${API}/refresh`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ refresh_token }),
  });
  
  if (!res.ok) {
    localStorage.removeItem("token");
    localStorage.removeItem("refresh_token");
    window.location.href = "/login";
    throw new Error("Session expired");
  }
  
  const data = await res.json();
  localStorage.setItem("token", data.token);
  localStorage.setItem("refresh_token", data.refresh_token);
  return data.token;
}

export async function apiFetch(path: string, options: RequestInit = {}) {
  const token = localStorage.getItem("token");
  
  const res = await fetch(`${API}${path}`, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
      ...(options.headers || {}),
    },
  });
  
  if (res.status === 401) {
    const newToken = await refreshToken();
    return fetch(`${API}${path}`, {
      ...options,
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${newToken}`,
        ...(options.headers || {}),
      },
    });
  }
  
  return res;
}