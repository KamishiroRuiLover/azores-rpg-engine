def std(brightness, environment, color, isEnvironmental):
    if isEnvironmental:
        retColor = (int(environment[0] * brightness), int(environment[1] * brightness), int(environment[2] * brightness))
    else:
        retColor = (color[0], color[1], color[2])
    return [1, retColor]


def blk(brightness, environment, color, isEnvironmental):
    return [0, (0,0,0)]


display_tags = {
    "std":std,
    "blk":blk
}