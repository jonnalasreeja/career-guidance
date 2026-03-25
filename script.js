document.getElementById("quizForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    const formData = {
        coding: parseInt(e.target.coding.value),
        problem: parseInt(e.target.problem.value),
        security: parseInt(e.target.security.value),
        network: parseInt(e.target.network.value),
        design: parseInt(e.target.design.value)
    };

    const response = await fetch("http://127.0.0.1:5000/recommend", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(formData)
    });

    const data = await response.json();
    document.getElementById("result").innerText = data.career;
});
