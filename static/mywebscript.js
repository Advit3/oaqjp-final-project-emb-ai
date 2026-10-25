document.getElementById("emotion-form").addEventListener("submit", async (event) => {
  event.preventDefault();
  const output = document.getElementById("result");
  const text = document.getElementById("text").value.trim();
  if (!text) {
    output.textContent = "Please enter text to analyze.";
    return;
  }
  output.textContent = "Analyzing…";
  try {
    const response = await fetch(`/emotionDetector?textToAnalyze=${encodeURIComponent(text)}`);
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || "Analysis failed.");
    output.textContent = `Dominant emotion: ${data.dominant_emotion}`;
  } catch (error) {
    output.textContent = error.message;
  }
});
