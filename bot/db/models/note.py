from sqlalchemy import String, Integer, BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from bot.db.models import Base


class Note(Base):
    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    title: Mapped[str] = mapped_column(String(64), nullable=False, default="Без названия")
    text: Mapped[str] = mapped_column(
        String(3000),
        nullable=False,
        default="Текст заметки (максимальное количество символов - 3000)",
    )
