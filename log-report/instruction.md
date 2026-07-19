There is an Apache-style access log at /app/access.log containing web traffic info. Analyze the traffic and summarize what you find
into /app/report.json in the following format.

The report must be a single JSON object with exactly these three fields:

- "total_requests": the total number of requests in the log.
- "unique_ips": the number of distinct client IP addresses in the log.
- "top_path": the request path that appears most frequently across all requests.

Success criteria:

1. /app/report.json exists and contains a single valid JSON object.
2. "total_requests" equals the number of requests in the log.
3. "unique_ips" equals the count of distinct client IP addresses.
4. "top_path" equals the most frequently requested path.