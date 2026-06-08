import streamlit as st
from streamlit.components.v1 import html
import random

st.title("My Cool Guessing Game")
st.subheader(
    "Guess a number between 1 and 100"
)
# check if secret has already been saved
if 'secret' not in st.session_state:
    st.session_state.secret = random.randint(1,100)



guess = st.number_input('Input a number between 1 and 100',min_value=1, max_value=100, step=1)

if st.button('Submit Guess'):
    st.write('You Guessed ', str(guess))
    if guess < st.session_state.secret:
        st.warning('Sorry, too low!')
        arrow_html = """
        <style>
        #arrow {position:fixed; left:50%; top:30%; transform:translate(-50%,-50%); width:120px; height:120px; pointer-events:none; z-index:1000000; animation: bounce 800ms ease-in-out 0s 3;}
        @keyframes bounce {0%{transform:translate(-50%,-50%) scale(0.6); opacity:0}30%{transform:translate(-50%,-60%) scale(1.1); opacity:1}60%{transform:translate(-50%,-50%) scale(0.95); opacity:1}100%{transform:translate(-50%,-50%) scale(0.6); opacity:0}}
        svg{width:100%;height:100%;filter:drop-shadow(0 0 8px rgba(0,0,0,0.5));}
        </style>
        <div id="arrow">
          <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <path d="M12 4l-8 8h5v8h6v-8h5l-8-8z" fill="#00AEEF"/>
          </svg>
        </div>
        """
        html(arrow_html, height=150)
    elif guess > st.session_state.secret:
        st.warning ('Sorry, too high!')
        arrow_html = """
        <style>
        #arrow {position:fixed; left:50%; top:30%; transform:translate(-50%,-50%); width:120px; height:120px; pointer-events:none; z-index:1000000; animation: bounce 800ms ease-in-out 0s 3;}
        @keyframes bounce {0%{transform:translate(-50%,-50%) scale(0.6); opacity:0}30%{transform:translate(-50%,-40%) scale(1.1); opacity:1}60%{transform:translate(-50%,-50%) scale(0.95); opacity:1}100%{transform:translate(-50%,-50%) scale(0.6); opacity:0}}
        svg{width:100%;height:100%;filter:drop-shadow(0 0 8px rgba(0,0,0,0.5));}
        </style>
        <div id="arrow">
          <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <path d="M12 20l8-8h-5v-8h-6v8H4l8 8z" fill="#FF3B30"/>
          </svg>
        </div>
        """
        html(arrow_html, height=150)
    else:
                st.success('Yay! You guessed it')
                # firework/confetti effect using canvas-confetti (CDN)
                firework_html = """
                <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
                <canvas id="confetti-canvas" style="position:fixed;pointer-events:none;left:0;top:0;width:100%;height:100%;z-index:999999;"></canvas>
                <script>
                const myCanvas = document.getElementById('confetti-canvas');
                const myConfetti = confetti.create(myCanvas, { resize: true, useWorker: true });
                function burst() {
                    for (let i = 0; i < 4; i++) {
                        myConfetti({
                            particleCount: 120,
                            startVelocity: 40,
                            spread: 360,
                            origin: { x: Math.random(), y: Math.random() * 0.5 }
                        });
                    }
                }
                burst();
                </script>
                """
                html(firework_html, height=300)

if guess==st.session_state.secret:
    if st.button('Play again'):
        st.session_state.secret = random.randint(1,100)
        st.rerun()
        