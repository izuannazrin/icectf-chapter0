while true; do
    for i in $(find . -name '*.zip'); do
        unzip $i
        rm $i
    done
done

# disebabkan malas, skrip ni tak akan berhenti. guna Ctrl+C.