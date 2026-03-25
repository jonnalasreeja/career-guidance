document.getElementById("quizForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const formData = {
        coding: e.target.coding.value,
        problem: e.target.problem.value,
        security: e.target.security.value
    };

    try {
        const response = await fetch("http://127.0.0.1:5000/api/recommend", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(formData)
        });

        const data = await response.json();

        document.getElementById("result").innerText = data.recommended_career;
        document.getElementById("resultBox").classList.remove("hidden");

    } catch (error) {
        console.error("Error:", error);
    }
});
