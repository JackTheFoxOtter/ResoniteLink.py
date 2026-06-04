from resonitelink.models.datamodel import Float3, Field_String
from resonitelink import ResoniteLinkClient, ResoniteLinkWebsocketClient
import asyncio


# Creates a new client that connects to ResoniteLink via websocket.
client = ResoniteLinkWebsocketClient()


@client.on_started
async def on_client_started(client : ResoniteLinkClient):
    """
    This async function is called by the client at the end of its startup sequence.
    You can use it to execute code once the client is up and running!

    """
    # Adds a new slot. Since no parent was specified, it will be added to the world root by default.
    slot = await client.add_slot(name="Hello World Slot", position=Float3(0, 1.5, 0))
    
    # Adds a TextRenderer component to the newly created slot.
    await slot.add_component("[FrooxEngine]FrooxEngine.TextRenderer",
        # Sets the initial value of the string field 'Text' on the component.
        Text=Field_String(value="Hello, world!")
    )
    
    # Stops the client manually. Without this, the client will run forever, which might be desired for some use-cases.
    await client.stop()


# Start the client, it will automatically connect to the first ResoniteLink session it discovers on the local network.
asyncio.run(client.start(auto_discover=True))
