document.getElementById("textForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const text = document.getElementById("textInput").value;
    
    const response = await fetch("/", {
        method: "POST",
        headers: { "Content-Type": "text/plain" },
        body: text
    });

    const result = await response.text();
    document.getElementById("response").innerText = result;
});
