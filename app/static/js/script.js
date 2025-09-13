async function sendData() {
    const text = document.getElementById("inputText").value;

    const response = await fetch("/api/echo", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text })
    });

    const data = await response.json();
    document.getElementById("response").innerText = JSON.stringify(data);
}
