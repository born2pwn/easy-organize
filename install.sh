echo "Installing easy-organize"

DEST="~/.local/share/easy-organize"

if [ ! -d "$DEST" ]; then
    mkdir -p "$DEST"
fi

cp -f ftypes.py organize.py ~/.local/share/easy-organize
sudo ln -s ~/.local/share/easy-organize/organize.py /usr/bin/organize
sudo chmod +x /usr/bin/organize

if [[ $? -eq 0 ]]; then
  echo "Successfully installed!"
fi