# /bin/bash
tmux kill-session -t felix-bot
tmux new-session -d -s felix-bot  -n server
tmux send -t server.0 cd SPACE ~/programming/felix-bot ENTER
tmux send -t server.0 python3 SPACE server.py ENTER
tmux new-window -d -t '=felix-bot' -n bot
tmux send -t bot.0 cd SPACE ~/programming/felix-bot ENTER
tmux send -t bot.0 node SPACE bot.js ENTER
