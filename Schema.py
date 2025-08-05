from pydantic import BaseModel, Field
class MoodResponse (BaseModel):
  mood_summary: str = Field(..., description="Reflection on how the user feel")

suggestion: str = Field(..., description="Helpful activity for user's current m ood")

log_status: str = Field(..., description="Confirmation of log entry")
