from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, DropDown, Group, Key, Match, ScratchPad, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.images import Img
from libqtile.log_utils import logger
from libqtile.widget import base

import os
import subprocess

from libqtile import hook

mod = "mod4"
myTerm = "kitty" 

keys = [

    Key([mod], "Return", 
        lazy.spawn(myTerm), 
        desc="Launch Terminal"),

    Key([mod, "shift"], "Return", 
        lazy.spawn("rofi -combi-modi window,drun,ssh -show combi 'Run: '"), 
        desc="Launch Dmenu"),

    Key([mod], "e",
        lazy.spawn("rofimoji"),
        desc="launch Rofimoji"),

    Key([mod], "d", 
        lazy.spawn("dmenu_run -p 'Run: '"), 
        desc="Launch Dmenu"),

    Key([mod], "r", 
        lazy.spawncmd(), 
        desc="Spawn a command using a prompt widget"),

    Key([mod, "mod1"], "p", 
        lazy.spawn("pcmanfm"), 
        desc="Launch PCManfm"),

    Key([mod, "mod1"], "f", 
        lazy.spawn("firefox"), 
        desc="Launch Firefox"),

    Key([mod, "mod1"], "g", 
        lazy.spawn("google-chrome-stable"), 
        desc="Launch Google Chrome"),

    Key([mod, "mod1"], "t", 
        lazy.spawn("telegram-desktop"), 
        desc="Launch Telegram-Desktop"),

    Key([mod, "shift"], "c",
        lazy.window.kill(), 
        desc="Kill focused window"),
    
    Key([mod, "shift"], "q", 
        lazy.shutdown(), 
        desc="Shutdown Qtile"),

    Key([mod, "shift"], "r", 
        lazy.reload_config(), 
        desc="Reload the config"),

    Key([mod], "Tab", 
        lazy.next_layout(), 
        desc="Toggle between layouts"),

    Key([mod, "shift"], "Tab",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    Key([], "XF86AudioLowerVolume", 
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -10%")),

    Key([], "XF86AudioRaiseVolume", 
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),

    Key([], "XF86AudioMute", 
        lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),

    Key([mod], "h", 
        lazy.layout.left(), 
        desc="Move focus to left"),

    Key([mod], "l", 
        lazy.layout.right(), 
        desc="Move focus to right"),

    Key([mod], "j", 
        lazy.layout.down(), 
        desc="Move focus down"),

    Key([mod], "k", 
        lazy.layout.up(), 
        desc="Move focus up"),

    Key([mod], "space", 
        lazy.layout.next(), 
        desc="Move window focus to other window"),

    Key([mod, "shift"], "h", 
        lazy.layout.shuffle_left(), 
        desc="Move window to the left"),

    Key([mod, "shift"], "l", 
        lazy.layout.shuffle_right(), 
        desc="Move window to the right"),

    Key([mod, "shift"], "j", 
        lazy.layout.shuffle_down(), 
        desc="Move window down"),

    Key([mod, "shift"], "k", 
        lazy.layout.shuffle_up(), 
        desc="Move window up"),

    Key([mod, "control"], "h", 
        lazy.layout.grow_left(), 
        desc="Grow window to the left"),

    Key([mod, "control"], "l", 
        lazy.layout.grow_right(), 
        desc="Grow window to the right"),

    Key([mod, "control"], "j", 
        lazy.layout.grow_down(), 
        desc="Grow window down"),

    Key([mod, "control"], "k", 
        lazy.layout.grow_up(), 
        desc="Grow window up"),

    Key([mod], "n", 
        lazy.layout.normalize(),
        desc="Reset all window sizes")]

groups = [Group('1', label="", layout='monadtall'),
          Group('2', label="", layout='monadtall', matches=[Match(wm_class='pcmanfm')]),
          Group('3', label="", layout='max', matches=[Match(wm_class='google-chrome-stable')]),
          Group('4', label="", layout='monadtall'),
          Group('5', label="", layout='monadtall'),
          Group('6', label="", layout='monadtall'),
          Group('7', label="", layout='monadtall'),
          Group('8', label="", layout='monadtall'),
          Group('9', label="", layout='monadtall', matches=[Match(wm_class='telegram-desktop')])]

group_names =  []
        
keynames = [i for i in "123456789"]
# group_labels = ["","","","","","","","",""]
group_labels = ["1","2","3","4","5","6","7","8","9"]
for g in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[g],
            label=group_labels[g],
        )
    )
# mod + i, moves screen to groups[i]
# mod + shift + i, moves screen with active tab to groups[i]
for keyname, group in zip(keynames, groups):
    keys.extend([
        Key([mod], keyname, lazy.group[group.name].toscreen()),
        Key([mod, "shift"], keyname, lazy.window.togroup(group.name)),
    ])

# Append scratchpad with dropdowns to groups
groups.append(ScratchPad('scratchpad', [
    DropDown('term', 'kitty', width=0.8, height=0.7, x=0.1, y=0.1, opacity=.85),
    DropDown('music', 'kitty -e ncmpcpp', width=0.8, height=0.7, x=0.1, y=0.1, opacity=1),
    DropDown('ranger', 'kitty -e ranger', width=0.8, height=0.7, x=0.1, y=0.1, opacity=1),
    DropDown('bitwarden', 'bitwarden-desktop', width=0.7, height=0.8, x=0.15, y=0.1, opacity=1),
]))
# extend keys list with keybinding for scratchpad
keys.extend([
    Key(["control"], "1", lazy.group['scratchpad'].dropdown_toggle('term')),
    Key(["control"], "2", lazy.group['scratchpad'].dropdown_toggle('music')),
    Key(["control"], "3", lazy.group['scratchpad'].dropdown_toggle('ranger')),
    Key(["control"], "4", lazy.group['scratchpad'].dropdown_toggle('bitwarden')),
    ])

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    layout.MonadTall(
        margin = 20 
        ),
    layout.Tile(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

###### Widgets for bar ######

widget_defaults = dict(
        font="Hurmit Nerd Font Bold",
    fontsize=13,
    padding=3,
    background="#2e3440",
    foreground="#2e3440",
)
extension_defaults = widget_defaults.copy()

## DRACULA COLOR SCHEME
color1 = '#6272a4'
color2 = '#8be9fd'
color3 = '#50fa7b'
color4 = '#ffb86c'
color5 = '#ff79c6'
color6 = '#bd93f9'
color7 = '#ff5555'
color8 = '#f1fa8c'
color9 = '#44475a'
color10 = '#f8f8f2'

# ## NORD COLOR SCHEME
# color1 = '#5E81AC'
# color2 = '#8FBCBB'
# color3 = '#B48EAD'
# color4 = '#EBCB8B'
# color5 = '#D08770'
# color6 = '#A3BE8C'
# color7 = '#BF616A'
# color8 = '#88C0D0'
# color9 = '#3B4252'

##BASIC COLORS
RED = '#FF0000'
DKRED = '#86080E'
GREEN = '#00FF00'
DKGREEN = '#338333'

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(
                    scale = .75,
                    ),
                widget.Spacer(length=15),
                widget.Volume(
                    fmt = ': {}',
                    #background = color5,
                    foreground = color5,
                    emoji = False,
                    ),
                widget.Spacer( length=15),
                widget.Mpd2(
                    max_chars = 32,
                    foreground = color4,
                    status_format = '  {play_status} {artist}  {title}',
                    update_interval = 1,
                    ),
                widget.Spacer(),
                widget.GroupBox(
                    font = "Hurmit Nerd Font",
                    fontsize = 18,
                    active = color1,
                    hide_unused = True,
                    #background = color1, 
                    highlight_method = 'line',
                    highlight_color = color1,
                    block_highlight_text_color = color10,
                    ),
                widget.Prompt(),
                widget.Spacer(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                    ),
                widget.OpenWeather(
                    fontsize = 14,
                    format = ' {main_temp} °{units_temperature}',
                    zip = 92253,
                    app_key = '6f535b0f14f17a54f2ecb8416c2ba28c',
                    city_id = 5364079,
                    metric = False,
                    update_interval = 600,
                    #background = color8,
                    foreground = color8,
                    ),
                widget.Spacer( length=15),
                widget.Clock(
                    fontsize = 13,
                    format=" %l:%M %p (%a, %b %d)",
                    #background = color6,
                    foreground = color6,
                    ),
                widget.Spacer( length=5),
                widget.Systray(
                    forground = color8,
                    ),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
