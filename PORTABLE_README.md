# Smart Expense Visualizer - Portable Version

## 🚀 Quick Start

### Windows Users:
1. **First Time Setup:**
   - Double-click `setup_portable.bat`
   - Wait for installation to complete

2. **Running the App:**
   - Double-click `run_app.bat`
   - The app will open in your web browser

### Mac/Linux Users:
1. **First Time Setup:**
   - Open terminal in this folder
   - Run: `chmod +x setup_portable.sh run_app.sh`
   - Run: `./setup_portable.sh`

2. **Running the App:**
   - Run: `./run_app.sh`
   - The app will open in your web browser

## 📋 Requirements

- **Python 3.8 or higher** must be installed on the target computer
- **Internet connection** (only needed for first-time setup)
- **At least 1GB free disk space**

## 🔧 What's Included

- ✅ Complete virtual environment with all dependencies
- ✅ All your expense data (preserved)
- ✅ Automatic setup scripts for Windows/Mac/Linux
- ✅ Easy-to-use run scripts
- ✅ All features: Calendar view, Charts, Smart Insights, Voice input, etc.

## 📁 Project Structure

```
smart_expense_visualizer/
├── app.py                    # Main application
├── setup_portable.bat       # Windows setup script
├── run_app.bat              # Windows run script
├── setup_portable.sh        # Mac/Linux setup script
├── run_app.sh               # Mac/Linux run script
├── requirements.txt         # Python dependencies
├── myenv/                   # Virtual environment (created after setup)
├── data/                    # Your expense data
├── reports/                 # Generated reports
├── components/              # UI components
├── features/                # App features
├── utils/                   # Utility functions
└── ...                      # Other project files
```

## 🛠️ Troubleshooting

### If setup fails:
1. **Python not found:** Install Python from https://python.org
2. **Permission denied (Mac/Linux):** Run `chmod +x *.sh`
3. **Virtual environment issues:** Delete `myenv` folder and run setup again

### If app won't start:
1. **Port already in use:** The app will try different ports automatically
2. **Browser doesn't open:** Manually go to http://localhost:8501
3. **Dependencies missing:** Run setup script again

## 💾 Data Persistence

- Your expense data is stored in the `data/` folder
- Reports are saved in the `reports/` folder
- All data travels with the USB drive
- No data is stored on the host computer

## 🔄 Updating the App

To update the app on a new computer:
1. Copy the entire folder to the new computer
2. Run the setup script (`setup_portable.bat` or `./setup_portable.sh`)
3. Run the app (`run_app.bat` or `./run_app.sh`)

## 📱 Features

- 📅 **Calendar View** - See expenses by day
- 📊 **Charts** - Visualize spending patterns
- 🧠 **Smart Insights** - AI-powered expense analysis
- ➕ **Add/Edit/Delete** - Manage expenses easily
- 🎤 **Voice Input** - Add expenses by speaking
- 📤 **Export Data** - Generate reports
- 🤖 **AI Chatbot** - Ask questions about your expenses

## 🆘 Support

If you encounter any issues:
1. Check the troubleshooting section above
2. Ensure Python 3.8+ is installed
3. Try running setup script again
4. Check that all files are present on the USB drive

---

**Note:** This portable version includes all necessary dependencies and will work on any computer with Python installed, without requiring internet access after the initial setup.
