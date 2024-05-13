#!/usr/bin/env sh

die() {
    echo "$1" && exit 1
}

shutdown() {
    kill -INT $1
}

run() {
    [ -z "$BOT_TOKEN" ] && die "BOT_TOKEN unset! Cannot continue"
    [ -z "$PICS_ROOT" ] && export PICS_ROOT=/pics/

    cd /dist
    python3 main.py &
    PID=$!

    trap 'shutdown $PID' SIGTERM
    wait $PID
}

run
