# agentiq/agents/memory_agent.py
import redis
import json
import os

# Initialize Redis client
redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
redis_client = redis.Redis.from_url(redis_url)

class MemoryAgent:
        def __init__(self, session_id):
                    self.session_id = session_id
                            self.key = f"agentiq:memory:{session_id}"

                                def add_message(self, role, content):
                                            history = self.get_history()
                                                    history.append({"role": role, "content": content})
                                                            redis_client.set(self.key, json.dumps(history))

                                                                def get_history(self):
                                                                            data = redis_client.get(self.key)
                                                                                    return json.loads(data) if data else []

                                                                                    def clear_memory(self):
                                                                                                redis_client.delete(self.key)
