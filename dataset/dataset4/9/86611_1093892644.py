asyncio.run(self.mqtt_client.publish_json(INGESTION_TOPIC, msg))