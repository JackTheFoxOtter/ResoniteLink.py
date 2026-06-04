from resonitelink.models.datamodel import Reference, Float3, Field_Uri
from resonitelink.proxies import ComponentProxy
from resonitelink import ResoniteLinkClient, ResoniteLinkWebsocketClient
from math import sin, cos, pi
import asyncio


# Creates a new client that connects to ResoniteLink via websocket.
client = ResoniteLinkWebsocketClient()


@client.on_started
async def on_client_started(client : ResoniteLinkClient):
    """
    This async function is called by the client at the end of its startup sequence.
    You can use it to execute code once the client is up and running!

    """
    def calc_signal(t : float, freq : float) -> float:
        """
        Produces a simple sin-wave tone at the specified frequency.

        Parameters
        ----------
        t : float
            The time at which the sample is taken.
        freq : float
            The frequency of the tone to generate.

        Returns
        -------
        The value of the signal at the specified sample time.

        """
        return sin(2 * pi * freq * t)

    def calc_amplitude(t, exp : float = 2.0) -> float:
        """
        Uses a simple shaping function to modulate the amplitude over time.

        Parameters
        ----------
        t : float
            The time at which the sample is taken.
        exp : float
            Exponent for shaping function.
        
        Returns
        -------
        The value of the shaping function at the specified sample time.

        """
        t = t * 2 - 1 # 0 ..  1 -> -1 ... 1
        return cos( pi * t / 2 ) ** exp

    freq = 440.0
    sample_rate=44100
    sample_count=sample_rate * 2

    # Compute the audio samples.
    samples = [ calc_signal(x / sample_rate, freq) * calc_amplitude(x / sample_rate) for x in range(sample_count) ]

    # Import the audio clip data into Resonite.
    asset_url = await client.import_audio_clip_raw_data(
        sample_rate=sample_rate, 
        sample_count=sample_count, 
        channel_count=1, 
        samples=samples
    )

    # Adds a new slot. Since no parent was specified, it will be added to the world root by default.
    slot = await client.add_slot(name="Imported Audio Clip", position=Float3(0, 1.5, 0))
    
    # Attaches a LegacyAudioPlayer component to the slot. The component sets up everything required on attach.
    audio_player = await slot.add_component(component_type="[FrooxEngine]FrooxEngine.LegacyAudioPlayer")
    
    # Find the StaticAudioClip components that was set up by the LegacyAudioPlayer. 
    audio_player_data = await audio_player.fetch_data()
    audio_clip = ComponentProxy.from_reference(client, audio_player_data.get_member(Reference, "AudioClip"))

    # Assign the URI of the imported asset to the StaticAudioClip component.
    await audio_clip.update_members(URL=Field_Uri(asset_url))

    # Stops the client manually. Without this, the client will run forever, which might be desired for some use-cases.
    await client.stop()


# Start the client, it will automatically connect to the first ResoniteLink session it discovers on the local network.
asyncio.run(client.start(auto_discover=True))
