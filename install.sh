#!/bin/bash
make_virtual_environment() {
    echo "Changing directory to src.."
    cd src || exit 1

    echo "Making a virtual environment.."
    python -m venv venv
}

install_dependencies() {
    echo "Activating the virtual environment.."
    source venv/bin/activate

    echo "Installing dependencies using pip.."
    pip install textual rich rich_pixels Pillow requests build
 
}

build_program() {
    echo "Building the program.."
    cd src
    source venv/bin/activate
    cd .. && python -m build
}

install_program() {
    echo "Installing the program system-wide.."
    deactivate
    su -c "pip install dist/ponytui-0.1-py3-none-any.whl --break-system-packages"

}

run_prompt() {
    while true; do
        echo "Installation is finished. Would you like to run the program now? (yes/y or no/n): "
        read answer
        case "$answer" in
            [Yy]* ) 
                ponytui
                break;;
            [Nn]* ) 
                echo "Exiting.."
                break;;
            * ) 
                echo "Please answer yes, y, no, or n.";;
        esac
    done
}

# Run the script
make_virtual_environment
install_dependencies
build_program
install_program
run_prompt