document.addEventListener('DOMContentLoaded', function() {
    // Settings menu logic
    const settingsBtn = document.getElementById('settings-menu-btn');
    const settingsDropdown = document.getElementById('settings-dropdown');
    const settingsDarkmode = document.getElementById('settings-darkmode');
    const settingsLanguage = document.getElementById('settings-language');
    const signinGoogle = document.getElementById('signin-google');
    const signinFacebook = document.getElementById('signin-facebook');
    const signinWhatsapp = document.getElementById('signin-whatsapp');

    settingsBtn.addEventListener('click', function(e) {
        e.stopPropagation();
        settingsDropdown.classList.toggle('active');
    });
    document.addEventListener('click', function(e) {
        if (!settingsDropdown.contains(e.target) && e.target !== settingsBtn) {
            settingsDropdown.classList.remove('active');
        }
    });
    // Sync dark mode toggle
    settingsDarkmode.checked = document.body.classList.contains('darkmode');
    settingsDarkmode.addEventListener('change', function() {
        document.body.classList.toggle('darkmode', settingsDarkmode.checked);
        document.getElementById('darkmode-btn').textContent = document.body.classList.contains('darkmode') ? '☀️' : '🌙';
    });
    // Sync dark mode button with menu
    document.getElementById('darkmode-btn').addEventListener('click', function() {
        document.body.classList.toggle('darkmode');
        settingsDarkmode.checked = document.body.classList.contains('darkmode');
        this.textContent = document.body.classList.contains('darkmode') ? '☀️' : '🌙';
    });
    // Language change stub
    settingsLanguage.addEventListener('change', function() {
        alert('Language switching is coming soon! Selected: ' + settingsLanguage.options[settingsLanguage.selectedIndex].text);
    });
    // Sign-in stubs
    signinGoogle.addEventListener('click', function() {
        alert('Google sign-in coming soon!');
    });
    signinFacebook.addEventListener('click', function() {
        alert('Facebook sign-in coming soon!');
    });
    signinWhatsapp.addEventListener('click', function() {
        alert('WhatsApp sign-in coming soon!');
    });

    // --- Existing chatbot logic below ---
    const chatWindow = document.getElementById('chat-window');
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');
    const clearBtn = document.getElementById('clear-btn');
    const helpBtn = document.getElementById('help-btn');
    const darkmodeBtn = document.getElementById('darkmode-btn');
    const sendSound = document.getElementById('send-sound');
    // Carousel logic
    const slides = document.querySelectorAll('.carousel-slide');
    let currentSlide = 0;
    function showSlide(idx) {
        slides.forEach((slide, i) => {
            slide.classList.toggle('active', i === idx);
        });
    }
    setInterval(() => {
        currentSlide = (currentSlide + 1) % slides.length;
        showSlide(currentSlide);
    }, 3500);

    // Info panel logic
    const infoFacts = document.querySelectorAll('.info-fact');
    let currentFact = 0;
    function showFact(idx) {
        infoFacts.forEach((fact, i) => {
            fact.classList.toggle('active', i === idx);
        });
    }
    setInterval(() => {
        currentFact = (currentFact + 1) % infoFacts.length;
        showFact(currentFact);
    }, 5000);

    // Typing indicator logic
    const typingIndicator = document.getElementById('typing-indicator');
    function showTypingIndicator(show) {
        if (show) {
            typingIndicator.classList.add('active');
        } else {
            typingIndicator.classList.remove('active');
        }
    }

    function appendMessage(sender, text) {
        const msgDiv = document.createElement('div');
        msgDiv.classList.add('message', sender);
        const iconSpan = document.createElement('span');
        iconSpan.classList.add('icon');
        iconSpan.textContent = sender === 'user' ? '👤' : '🤖';
        const bubbleDiv = document.createElement('div');
        bubbleDiv.classList.add('bubble');
        bubbleDiv.textContent = text;
        if (sender === 'user') {
            msgDiv.appendChild(bubbleDiv);
            msgDiv.appendChild(iconSpan);
        } else {
            msgDiv.appendChild(iconSpan);
            msgDiv.appendChild(bubbleDiv);
        }
        chatWindow.appendChild(msgDiv);
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }

    function sendMessage() {
        const message = userInput.value.trim();
        if (!message) return;
        appendMessage('user', message);
        userInput.value = '';
        if (sendSound) {
            sendSound.currentTime = 0;
            sendSound.play();
        }
        showTypingIndicator(true);
        fetch('/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message })
        })
        .then(res => res.json())
        .then(data => {
            showTypingIndicator(false);
            appendMessage('bot', data.response);
        })
        .catch(() => {
            showTypingIndicator(false);
            appendMessage('bot', 'Sorry, there was an error connecting to the server.');
        });
    }

    // Welcome message
    appendMessage('bot', '👋 Welcome to Civic Chat Bot! I can help you with information about government schemes, voting rights, public schemes, and constitutional laws. Type your question below!');

    sendBtn.addEventListener('click', sendMessage);
    userInput.addEventListener('keydown', function(e) {
        if (e.key === 'Enter') sendMessage();
    });

    // Clear chat functionality
    clearBtn.addEventListener('click', function() {
        chatWindow.innerHTML = '';
        appendMessage('bot', '👋 Welcome to Civic Chat Bot! I can help you with information about government schemes, voting rights, public schemes, and constitutional laws. Type your question below!');
    });

    // Help/info functionality
    helpBtn.addEventListener('click', function() {
        alert('Civic Chat Bot can answer questions about:\n\n- Voting rights and Voter ID\n- Major government schemes (PMAY, Ujjwala, Jan Dhan, Ayushman Bharat, PM-KISAN, scholarships, Mudra, Skill India, Digital India, Make in India, Startup India, Swachh Bharat, Beti Bachao Beti Padhao, Atma Nirbhar Bharat, National Health Mission, Mid Day Meal, Old Age Pension, etc.)\n- Public schemes (ration card, pension)\n- Judiciary and important laws (Supreme Court, High Court, PIL, Habeas Corpus, landmark judgments, IPC, CrPC, RTI, RTE, Dowry Prohibition, POCSO, SC/ST Act, etc.)\n- Constitution (Fundamental Rights, Directive Principles, Fundamental Duties, Preamble, Articles)\n\nTry asking: "What is Ayushman Bharat?", "What are fundamental rights?", "How to get a Voter ID?", "Tell me about Article 21"');
    });

    // Dark mode toggle (syncs with menu)
    darkmodeBtn.addEventListener('click', function() {
        document.body.classList.toggle('darkmode');
        settingsDarkmode.checked = document.body.classList.contains('darkmode');
        this.textContent = document.body.classList.contains('darkmode') ? '☀️' : '🌙';
    });
});
