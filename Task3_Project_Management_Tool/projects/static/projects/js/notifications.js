// Polls the server every 15 seconds for unread notification count.
// This is the "real-time updates" bonus from the brief - not a true
// websocket connection, but gives that live-update feel without
// needing a separate ASGI/channels server running.

function pollNotifications() {
    fetch('/notifications/poll/')
        .then(response => response.json())
        .then(data => {
            const badge = document.getElementById('notif-badge');
            if (!badge) return;
            if (data.unread_count > 0) {
                badge.textContent = data.unread_count;
                badge.style.display = 'inline-block';
            } else {
                badge.style.display = 'none';
            }
        })
        .catch(() => {});
}

document.addEventListener('DOMContentLoaded', () => {
    pollNotifications();
    setInterval(pollNotifications, 15000);
});
