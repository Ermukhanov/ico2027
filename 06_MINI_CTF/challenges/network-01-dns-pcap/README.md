# Фрагменты в DNS-запросах

**Категория:** Networking / PCAP. **Цель:** собрать hex-части из DNS query name по порядку времени и декодировать байты.

Начни с `file challenge/queries.pcap`, `tshark -r challenge/queries.pcap -Y dns -T fields -e frame.time -e dns.qry.name`. Найди полные имена с суффиксом `.lab.test`, отсортируй запросы и собери hex-метки. Весь трафик синтетический, использует документационные адреса RFC 5737 и не содержит настоящих сетевых соединений.
