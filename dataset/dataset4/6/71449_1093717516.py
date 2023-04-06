button = Button(...)
bindtags = button.bindtags()
button.bindtags(bindtags[:1] + ['MyButton'] + bindtags[1:])
root.bind_class('MyButton', ...)