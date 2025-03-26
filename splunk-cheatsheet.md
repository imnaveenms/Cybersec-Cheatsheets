# 📌 Splunk Cheat Sheet
### 🔍 Basic Searches
```spl
index=* source="auth.log"
index=firewall action=blocked
```
### 📊 Field Extraction
```spl
index=web_logs | table _time, user, src_ip, uri
```
### 🚀 Advanced Queries
```spl
index=malware_logs | stats count by file_hash
```
