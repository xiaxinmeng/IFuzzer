import asyncio
from unittest.mock import MagicMock, AsyncMock, patch


class Database:
    pass


async def mock_database():
    with patch(f"{__name__}.Database") as db:
        db.configure_mock(
            **{
                "connection.return_value.__aenter__.return_value": MagicMock(
                    **{
                        "query.return_value.__aenter__.return_value": AsyncMock(
                            return_value=[1]
                        )
                    }
                )
            }
        )

        async with db.connection() as conn:
            async with conn.query() as query:
                result = await query("select * from people")
                assert result == [1]
                print(f"Result : {result}")


asyncio.run(mock_database())