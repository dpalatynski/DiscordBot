def check_for_channel(channel_id):
    if not channel_id:
        is_channel = None
    elif channel_id[1] == '#':
        is_channel = True
    else:
        is_channel = False

    return is_channel
