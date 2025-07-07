#!/bin/bash

# from a list of 25 fruits, build a for loop that print out each fruit in the list with a running number and a colon with the fruit name
# using shell array and loop with counter

generate_fruit_list() {
    # Array of 25 fruits
    local all_fruits=(
        "apple"
        "banana"
        "cherry"
        "date"
        "elderberry"
        "fig"
        "grape"
        "honeydew"
        "kiwi"
        "lemon"
        "mango"
        "nectarine"
        "orange"
        "papaya"
        "quince"
        "raspberry"
        "strawberry"
        "tangerine"
        "ugli fruit"
        "vanilla bean"
        "watermelon"
        "xigua"
        "yellow passion fruit"
        "zucchini flower"
    )
    
    # Shuffle array and select first 15 fruits
    local shuffled_fruits=($(printf '%s\n' "${all_fruits[@]}" | shuf | head -15))
    
    # Return the selected fruits (pass by reference using global array)
    selected_fruits=("${shuffled_fruits[@]}")
}

main() {
    # Generate random fruit list
    generate_fruit_list
    
    # Print fruits with running numbers using enumerate-like approach
    local index=1
    for fruit in "${selected_fruits[@]}"; do
        printf "%d: %s\n" "$index" "$fruit"
        ((index++))
    done
}

# Run main function if script is executed directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
