const iframeRef = document.getElementById("myIframe"); //iFrameIdExample

const handleMessage = (event) => {
  if (event.source === iframeRef.contentWindow) {
    const data = event.data;
    switch (data.action) {
      case "onAnalysisStart":
        console.log("onAnalysisStart", data?.analysisData);
        break;
      case "onHealthAnalysisFinished":
        console.log("onHealthAnalysisFinished", data?.analysisData);
        break;
      case "onVoiceAnalysisFinished":
        console.log("onVoiceAnalysisFinished", data?.analysisData);
        break;
      case "failedToGetResults":
        console.log("failedToGetResults", data?.analysisData);
        break;
      case "failedToLoadPage":
        console.log("failedToLoadPage", data?.analysisData);
        break;
      case "failedToGetVoiceAnalysisResult":
        console.log("failedToGetVoiceAnalysisResult", data?.analysisData);
        break;
      default:
        break;
    }
  }
};

window.addEventListener("message", handleMessage);
