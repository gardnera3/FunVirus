# styles.py

def get_checkbox_styles(checked_path, unchecked_path):
    return f"""
    QCheckBox::indicator {{
        width: 25px;
        height: 20px;
    }}
    QCheckBox::indicator:checked {{
        image: url({checked_path});
    }}
    QCheckBox::indicator:unchecked {{
        image: url({unchecked_path});
    }}
    """

def get_combobox_styles(arrow_path):
    return f"""
    QComboBox::down-arrow {{
        image: url('{arrow_path}');
        width: 20px;
        height: 20px;
    }}
    QComboBox::drop-down {{
        subcontrol-origin: padding;
        subcontrol-position: center right;
        border-left: 0px;
        width: 12px;
    }}
    QComboBox{{
        border: 2px solid #424549;
        border-radius: 5px;
        selection-background-color: #7289da;
        selection-color: #424549;
    }}
    QComboBox QAbstractItemView {{
        background-color: #1e2124;
        color: white;
        selection-background-color: #7289da;
        selection-color: white;
        border: 1px solid #444;
        padding: 5px;
        margin: 0px;
        outline: 0px;
    }}
    """
