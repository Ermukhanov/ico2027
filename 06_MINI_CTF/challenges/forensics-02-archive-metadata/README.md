# Комментарий ZIP как улика

**Категория:** Forensics. **Цель:** исследовать структуру и метаданные контейнера, не только распакованные файлы.

Начни с `file challenge/evidence.zip`, `unzip -l challenge/evidence.zip`, `unzip -z challenge/evidence.zip`. Сам архив не повреждён; решатель читает комментарий стандартной библиотекой Python.
