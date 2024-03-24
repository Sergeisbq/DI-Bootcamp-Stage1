import { useEffect, useRef } from "react";

const ParentComponent = () => {
  const iframeRef = useRef(null);

  const handleMessage = (event) => {
    if (event.source === iframeRef.current.contentWindow) {
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

  useEffect(() => {
    window.addEventListener("message", handleMessage);
    return () => {
      window.removeEventListener("message", handleMessage);
    };
  }, []);

  return (
    <div>
      <iframe
        title="iFrame"
        ref={iframeRef}
        src="https://staging.bizbaz.tech/face-scan-iframe?videoToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpbnN0aXR1dGlvbklkIjoiNjNmMzhlNjRlMjUyODIxN2QxYTMxYzc4IiwiY2xpZW50SWQiOjQ3ODY1Mywidm9pY2VBbmFseXNpc1R5cGUiOiJjYW5kaWRhdGVTdWNjZXNzL2dlbmVyYWwiLCJpYXQiOjE3MTA3Njc1OTQsImV4cCI6MTcxMDc3MDI5NH0.fnd0PzOr6Zf0t2tctYS9G_Y8TJqzHqUN8xTScvrdsak&showResults=true&isVoiceAnalysisOn=true"
        width="1200"
        height="400"
        allow="camera; microphone"
      />
    </div>
  );
};

export default ParentComponent;
