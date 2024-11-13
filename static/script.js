<script>
    document.getElementById("contact-form").addEventListener("submit", function(event) {
        event.preventDefault(); // Останавливаем стандартное поведение отправки формы

        // Получаем значение email
        const email = document.getElementById("email").value;

        // Отправляем запрос на сервер
        fetch("/submit-email", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ email: email })
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === "success") {
                // Показ сообщения благодарности при успешной отправке
                const thankYouMessage = document.getElementById("thank-you-message");
                thankYouMessage.style.display = "block";

                setTimeout(() => {
                    thankYouMessage.style.display = "none";
                }, 3000);
            }
        })
        .catch(error => console.error("Ошибка при отправке данных:", error));
    });
</script>
