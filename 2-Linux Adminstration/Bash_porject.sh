#!/bin/bash

LOG_FILE="/var/log/bash-project/activity.log"

if [[ ! -w "$LOG_FILE" ]]; then
    echo "Error: Cannot write to Activity Log"
    exit 1
fi

echo "$(date '+%Y-%m-%d %H:%M:%S') | $MODE | Application Started" >> "$LOG_FILE"

USERNAME="user_test"

if [[ $EUID -eq 0 ]]; then
    MODE="ADMIN"
else
    MODE="USER"
fi   

if ! id -u "$USERNAME" &>/dev/null; then
    if [[ $MODE == "USER" ]]; then
        echo "User does not Exist"
        echo "sign in as a ADMIN to Create USER"
        exit 1
    elif [[ $MODE == "ADMIN" ]]; then     
        echo "Create User..."
        if adduser --disabled-password --gecos "" "$USERNAME"; then 
            echo "User was Created"
        else 
            echo "User fail Creation"   
            exit 1  
        fi
    fi     
fi 

function delete_user(){

    if ! id -u "$USERNAME" &>/dev/null; then
        echo "User does not Exist"
        return 1
    else 
        echo "5- User Delete"
        deluser --remove-home $USERNAME
        return 0
    fi
}

function cpu_usage() {

    read -r _ user nice system idle iowait irq softirq steal _ \
        < /proc/stat

    total1=$((user + nice + system + idle + iowait + irq + softirq + steal))
    idle1=$((idle + iowait))

    sleep 1

    read -r _ user nice system idle iowait irq softirq steal _ \
        < /proc/stat

    total2=$((user + nice + system + idle + iowait + irq + softirq + steal))
    idle2=$((idle + iowait))

    total_diff=$((total2 - total1))
    idle_diff=$((idle2 - idle1))

    if (( total_diff > 0 )); then
        usage=$((100 * (total_diff - idle_diff) / total_diff))
        echo "CPU Usage: $usage%"
    else
        echo "CPU Usage: Unavailable"
    fi
}

cpu_frequency() {

    local frequency
    local cpu=0

    while read -r frequency; do

        echo "CPU $cpu Frequency: $frequency MHz"

        ((cpu++))

    done < <(grep "cpu MHz" /proc/cpuinfo | cut -d ':' -f 2)

    if ((cpu == 0)); then
        echo "CPU Frequency: Unavailable"
        return 1
    fi
}

ram_info() {

    local total available used percentage

    total=$(grep '^MemTotal:' /proc/meminfo | tr -s ' ' | cut -d ' ' -f 2)

    available=$(grep '^MemAvailable:' /proc/meminfo | tr -s ' ' | cut -d ' ' -f 2)

    if [[ ! "$total" =~ ^[0-9]+$ || ! "$available" =~ ^[0-9]+$ || "$total" -eq 0 ]]; then
        echo "RAM Information: Unavailable"
        return 1
    fi

    used=$((total - available))
    percentage=$((used * 100 / total))

    echo "RAM Usage: $percentage%"

    printf "Used RAM: %d.%02d GiB\n" \
        "$((used / 1048576))" \
        "$((used % 1048576 * 100 / 1048576))"
}

disk_info() {

    local disk_usage
    local free_space

    read -r disk_usage free_space < <(
        df -h --output=pcent,avail / | tail -n 1
    )

    if [[ -z "$disk_usage" || -z "$free_space" ]]; then
        echo "Disk Information: Unavailable"
        return 1
    fi

    echo "Disk Usage: $disk_usage"
    echo "Free Disk Space: $free_space"
}

devices_management() {

    while true; do

        echo "===== Devices Management ====="
        echo "1- Change CPU Policy"
        echo "2- Set Battery Threshold (60%)"
        echo "3- Control Caps Lock LED"
        echo "0- Back"

        read -rp "Enter Choice: " choice

        case "$choice" in

            1)
                
                echo "===== CPU POLICY ====="

                policy="/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor"

                if [[ -f "$policy" ]]; then

                    echo "1- Performance"
                    echo "2- Powersave"

                    read -rp "Choose Policy: " cpu_choice

                    case "$cpu_choice" in
                        1) governor="performance" ;;
                        2) governor="powersave" ;;
                        *)
                            echo "Invalid Choice"
                            continue
                            ;;
                    esac

                    if grep -qw "$governor" \
                        /sys/devices/system/cpu/cpu0/cpufreq/scaling_available_governors; then

                        if echo "$governor" > "$policy"; then
                            echo "CPU Policy Changed to: $governor"
                        else
                            echo "Failed to change CPU Policy"
                        fi

                    else
                        echo "This CPU Policy is Not Supported"
                    fi

                else
                    echo "CPU Policy Control: Not Supported"
                fi
                ;;

            2)

                echo "===== BATTERY THRESHOLD ====="

                threshold="/sys/class/power_supply/BAT0/charge_control_end_threshold"

                if [[ -f "$threshold" ]]; then

                    if echo 60 > "$threshold"; then
                        echo "Battery Threshold Set to 60%"
                    else
                        echo "Failed to set Battery Threshold"
                    fi

                else
                    echo "Battery Threshold Control: Not Supported"
                fi
                ;;

            3)
                echo "$(date '+%F %T') | $MODE | Caps Lock LED ON | SUCCESS" >> "$LOG_FILE"
                echo "===== CAPS LOCK LED ====="

                led="/sys/class/leds/input2::capslock/brightness"

                if [[ -f "$led" ]]; then

                    echo "1- LED ON"
                    echo "2- LED OFF"

                    read -rp "Enter Choice: " led_choice

                    case "$led_choice" in
                        1)
                            if echo 1 > "$led"; then
                                echo "Caps Lock LED: ON"
                            else
                                echo "Failed to turn LED ON"
                            fi
                            ;;

                        2)
                            if echo 0 > "$led"; then
                                echo "Caps Lock LED: OFF"
                            else
                                echo "Failed to turn LED OFF"
                            fi
                            ;;

                        *)
                            echo "Invalid Choice"
                            ;;
                    esac

                else
                    echo "Caps Lock LED Control: Not Supported"
                fi
                ;;

            0)
                break
                ;;

            *)
                echo "Invalid Choice"
                ;;

        esac

    done
}

network_info() {

    echo "===== NETWORK INFORMATION ====="

    # IP Address
    echo "IP Address: $(hostname -I)"

    # DNS
    dns=$(grep -m 1 '^nameserver' /etc/resolv.conf | tr -s ' ' | cut -d ' ' -f 2)
    echo "DNS Server: $dns"

    # Network Interface
    interface=$(ip route show default | grep -oP 'dev \K\S+' | head -n 1)

    if [[ -z "$interface" ]]; then
        echo "Network Interface: Not Available"
        return 1
    fi

    # First Reading
    read -r name rx1 _ _ _ _ _ _ _ tx1 _ < <(
        grep "$interface:" /proc/net/dev
    )

    sleep 1

    # Second Reading
    read -r name rx2 _ _ _ _ _ _ _ tx2 _ < <(
        grep "$interface:" /proc/net/dev
    )

    # Calculate
    download=$(((rx2 - rx1) / 1024))
    upload=$(((tx2 - tx1) / 1024))

    echo "Download Rate: $download KiB/s"
    echo "Upload Rate: $upload KiB/s"
}



while true; do 

    echo "===================="
    echo "Linux System Manager" 
    echo "Current Mode: $MODE"
    echo "===================="

    echo "1- System Information"
    echo "2- Network Information"
    
    if [[ $MODE == "ADMIN" ]]; then 
        echo "3- Kernal Logs"
        echo "4- Device Managment"
        echo "5- User Delete"
        echo "6- Reboot"
        echo "7- Shutdown"
        echo "8- View Activity Log"
    fi 
    echo "0- Exit"

    read -rp "Enter your choice: " choice

    case "$choice" in
        1)
            echo "$(date '+%Y-%m-%d %H:%M:%S') | $MODE | System Information Selected" >> "$LOG_FILE"
            
            echo "=====   CPU Information   ======"
            cpu_usage
            cpu_frequency
            echo "CPU Temperature: Invalid Data"
            ram_info
            disk_info
            ;;
        2)  
            echo "$(date '+%Y-%m-%d %H:%M:%S') | $MODE | Network Information Selected" >> "$LOG_FILE"
            network_info
            ;;
        3)

            if [[ "$MODE" == "ADMIN" ]]; then

                echo "$(date '+%F %T') | $MODE | Kernel Logs Opened" >> "$LOG_FILE"

            echo "===== REAL-TIME KERNEL LOGS ====="
            echo "Press ENTER to return to Main Menu"

            journalctl -k -b -f -n 10 &
            log_pid=$!

            read -r

            kill "$log_pid" 2>/dev/null
            wait "$log_pid" 2>/dev/null

            echo "$(date '+%F %T') | $MODE | Kernel Logs Closed" >> "$LOG_FILE"

            echo "Returning to Main Menu..."

            else
                echo "Access Denied!"
                echo "$(date '+%Y-%m-%d %H:%M:%S') | $MODE | Kernel Logs Denied" >> "$LOG_FILE"
            fi
            ;;
        
        4)
            if [[ "$MODE" == "ADMIN" ]]; then

                echo "$(date '+%Y-%m-%d %H:%M:%S') | $MODE | Devices Management Selected" >> "$LOG_FILE"

                devices_management

            else
                echo "Access Denied!"
                echo "$(date '+%Y-%m-%d %H:%M:%S') | $MODE | Devices Management Denied" >> "$LOG_FILE"
            fi
            ;;

        5)
            if [[ $MODE == "ADMIN" ]]; then     
            delete_user
            else 
                echo "access denied"
            fi
            ;;
        6)
            if [[ "$MODE" == "ADMIN" ]]; then

                read -rp "Are you sure you want to reboot? (yes/no): " confirm

                if [[ "$confirm" == "yes" ]]; then
                    reboot
                else
                    echo "Reboot Cancelled"
                fi

            else
                echo "Access Denied! Admin Only."
            fi
            ;;

        7)
            if [[ "$MODE" == "ADMIN" ]]; then

                read -rp "Are you sure you want to shutdown? (yes/no): " confirm

                if [[ "$confirm" == "yes" ]]; then
                    systemctl poweroff
                else
                    echo "Shutdown Cancelled"
                fi

            else
                echo "Access Denied! Admin Only."
            fi
            ;;
        8)
            echo "$(date '+%F %T') | $MODE | Activity Log Viewed" >> "$LOG_FILE"

            echo "===== ACTIVITY LOG ====="
            echo "1- Show All Logs"
            echo "2- Show Last 10 Lines"

            read -rp "Enter Choice: " log_choice

            case "$log_choice" in

                1)
                    cat "$LOG_FILE"
                    ;;

                2)
                    tail -n 10 "$LOG_FILE"
                    ;;

                *)
                    echo "Invalid Choice"
                    ;;
            esac
            ;;
        0)
            if > "$LOG_FILE"; then
                echo "Activity Log Cleared Successfully."
            else
                echo "Failed to Clear Activity Log."
            fi

            echo "Goodbye!"
            break
            ;;   
        *)
            echo "Invalid Choice"
            ;;
    esac

done     