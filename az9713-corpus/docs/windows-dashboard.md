---
repo: windows-dashboard
description: 
language: Python
stars: 0
forks: 0
created: 2025-06-14
updated: 2025-06-14
topics: 
is_fork: False
kb: 16
---

# windows-dashboard
# Windows Resource Monitor Dashboard

A real-time system resource monitoring application for Windows laptops built with Python and Tkinter.

## Features

- **Real-time Monitoring**: Live tracking of system resources with automatic updates
- **CPU Usage**: Monitor CPU utilization percentage with historical charts
- **Memory Usage**: Track RAM consumption and availability
- **Disk Usage**: Monitor disk space utilization
- **Network Activity**: Track network bytes sent and received
- **System Information**: Display comprehensive system details
- **Interactive Charts**: Real-time matplotlib charts for visual monitoring
- **Cross-platform**: Works on Windows, Linux, and macOS

## Screenshots

The dashboard displays:
- System information panel (platform, CPU, memory specs)
- Current resource usage metrics
- Real-time charts for CPU, memory, disk, and network usage

## Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Required Packages

- `psutil>=5.8.0` - Cross-platform system and process utilities
- `matplotlib>=3.5.0` - Plotting library for real-time charts

## Usage

### Running the Dashboard

```bash
python dashboard.py
```

The application will open a GUI window displaying:
1. **System Information**: Hardware and OS details
2. **Current Metrics**: Real-time resource usage percentages
3. **Historical Charts**: Four real-time charts showing resource trends

### Features Breakdown

#### System Information Panel
- Operating system details
- Hostname and processor information
- CPU core count (physical and logical)
- Total memory and disk capacity

#### Resource Monitoring
- **CPU Usage**: Percentage utilization updated every 2 seconds
- **Memory Usage**: RAM consumption percentage
- **Disk Usage**: Storage utilization percentage
- **Network Activity**: Bytes sent/received in real-time

#### Real-time Charts
- CPU usage trend over time
- Memory usage history
- Disk usage monitoring
- Network activity (separate lines for sent/received data)

## Code Structure

```
windows_dashboard/
├── dashboard.py          # Main application file
├── test_dashboard.py     # Comprehensive test suite
├── requirements.txt      # Python dependencies
├── README.md            # This documentation
└── docs/
    ├── API.md           # API documentation
    └── CONTRIBUTING.md  # Contributing guidelines
```

### Main Components

#### ResourceMonitor Class
- `get_cpu_usage()`: Returns current CPU utilization
- `get_memory_usage()`: Returns current memory usage percentage
- `get_disk_usage()`: Returns disk usage percentage
- `get_network_usage()`: Returns network bytes sent/received
- `get_system_info()`: Returns comprehensive system information
- `update_data()`: Updates all resource data and stores in deques

#### DashboardGUI Class
- `setup_ui()`: Creates the main GUI layout
- `setup_system_info()`: Displays system information
- `setup_metrics()`: Creates current metrics labels
- `setup_charts()`: Initializes matplotlib charts
- `update_charts()`: Refreshes chart data
- `monitoring_thread()`: Background thread for continuous monitoring

## Testing

The project includes comprehensive unit tests covering:

### Test Coverage
- ResourceMonitor functionality
- Data collection methods
- GUI component initialization
- Integration testing
- Mock-based testing for system calls

### Running Tests

```bash
# Run all tests
python test_dashboard.py

# Run tests with virtual display (Linux)
xvfb-run -a python test_dashboard.py

# Run specific test class
python -m unittest test_dashboard.TestResourceMonitor
```

### Test Classes
- `TestResourceMonitor`: Tests core monitoring functionality
- `TestDashboardGUI`: Tests GUI components
- `TestIntegration`: End-to-end integration tests

## Performance

- **Update Frequency**: 2-second intervals for resource monitoring
- **Memory Usage**: Maintains sliding window of last 50 data points
- **CPU Impact**: Minimal system overhead (~1-2% CPU usage)
- **Thread Safety**: Uses daemon threads for background monitoring

## Compatibility

### Operating Systems
- **Windows**: Full functionality (primary target)
- **Linux**: Full functionality with virtual display for GUI
- **macOS**: Compatible with minor path adjustments

### Python Versions
- Python 3.7+
- Tested on Python 3.8, 3.9, 3.10, 3.11

## Troubleshooting

### Common Issues

1. **Import Error - psutil**
   ```bash
   pip install psutil
   ```

2. **GUI Display Issues on Linux**
   ```bash
   # Install virtual display
   sudo apt-get install xvfb
   # Run with virtual display
   xvfb-run -a python dashboard.py
   ```

3. **Permission Issues**
   - Ensure user has permission to access system resources
   - Some network monitoring features may require elevated privileges

### Debug Mode

For debugging, you can modify the update interval in `dashboard.py`:
```python
time.sleep(2)  # Change to desired interval in seconds
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Clone repository
git clone <repository-url>
cd windows_dashboard

# Install dependencies
pip install -r requirements.txt

# Run tests
python test_dashboard.py
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [psutil](https://github.com/giampaolo/psutil) for cross-platform system monitoring
- Uses [matplotlib](https://matplotlib.org/) for real-time charting
- GUI built with Python's built-in tkinter library

## Future Enhancements

- Export data to CSV/JSON formats
- Configurable alert thresholds
- Process-level monitoring
- Historical data persistence
- Web-based dashboard option
- Docker containerization support