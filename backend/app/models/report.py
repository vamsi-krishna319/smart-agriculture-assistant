from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.database.database import Base


class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)

    analysis_id = Column(
        Integer,
        ForeignKey("analysis.id"),
        nullable=False,
        unique=True
    )

    # Complete AI generated report (Markdown/Text)
    report_text = Column(Text, nullable=False)

    # PDF will be generated later
    pdf_path = Column(String, nullable=True)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    analysis = relationship(
        "Analysis",
        back_populates="report"
    )