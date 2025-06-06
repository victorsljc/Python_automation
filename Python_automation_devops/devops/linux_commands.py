"""
# Navigation
pwd                 # Print working directory
ls -la              # List all files (including hidden) with details
cd /var/log         # Change directory
cd ~                # Go to home directory

# File operations
touch file.txt      # Create empty file
mkdir new_dir       # Create directory
cp file.txt file_backup.txt  # Copy file
mv file.txt renamed_file.txt # Move/rename file
rm file.txt         # Remove file (be careful!)
cat file.txt        # View file content
less file.txt      # View file with pagination
head -n 5 file.txt  # Show first 5 lines
tail -f /var/log/syslog # Follow log file in real-time

# System info
uname -a            # Show system information
df -h               # Show disk space in human-readable format
free -m             # Show memory usage in MB
uptime              # Show system uptime and load average

# User management
sudo adduser newuser          # Add new user
sudo usermod -aG sudo newuser # Add user to sudo group
sudo passwd newuser           # Change user password
whoami                        # Show current user
id                            # Show user and group info

# Permission management
chmod 755 script.sh           # Change file permissions (rwxr-xr-x)
chown user:group file.txt     # Change file owner and group
ls -l                         # View permissions
umask                         # Show default permission mask

Package Management (Ubuntu/Debian):
sudo apt update               # Update package list
sudo apt upgrade              # Upgrade installed packages
sudo apt install nginx        # Install package
sudo apt remove nginx         # Remove package
sudo apt search "python*"     # Search for packages
sudo apt autoremove           # Remove unused packages

Process Management
ps aux                 # List all running processes
top                    # Interactive process viewer (q to quit)
htop                   # Enhanced process viewer (install with apt install htop)
kill -9 PID            # Force kill process by PID
pkill process_name     # Kill process by name
killall process_name   # Kill all processes with name
bg                     # Put process in background
fg                     # Bring process to foreground
jobs                   # List background jobs

Networking
ifconfig               # Network interfaces (or ip a)
ping google.com        # Test connectivity
netstat -tulnp         # Show listening ports (or ss -tulnp)
traceroute google.com  # Trace network path (or tracepath)
dig google.com         # DNS lookup
nslookup google.com    # Alternative DNS lookup
curl ifconfig.me       # Get public IP
wget http://example.com/file.zip # Download file
ssh user@host          # Connect to remote host
scp file.txt user@host:/path/ # Copy file to remote host

Text Processing

grep "error" /var/log/syslog  # Search for pattern in file
grep -r "pattern" /path/      # Recursive search
awk '{print $1}' file.txt     # Print first column
sed 's/foo/bar/g' file.txt    # Replace text in file
sort file.txt                # Sort lines
uniq file.txt                # Remove duplicate lines
wc -l file.txt               # Count lines
cut -d: -f1 /etc/passwd      # Extract first field delimited by :

version control

git clone https://github.com/user/repo.git
git status
git add .
git commit -m "message"
git push origin main

ansible commands
ansible all -m ping
ansible-playbook playbook.yml

docker
docker ps
docker run -d nginx
docker exec -it container_id bash
docker build -t myimage .


"""