import asyncio

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler

TOKEN = "8777970712:AAHeyS6TD7w2deMGdSWwMKcJscBRt5O7Br0"
questions = [
{
    "question": "What is the primary mechanism of action of morphine?",
    "options": [
        "A) COX inhibition",
        "B) Opioid receptor agonist",
        "C) Sodium channel blocker",
        "D) Calcium channel blocker"
    ],
    "answer": "B"
},
{
    "question": "Which drug is classified as an NSAID?",
    "options": [
        "A) Morphine",
        "B) Fentanyl",
        "C) Ibuprofen",
        "D) Tramadol"
    ],
    "answer": "C"
},
{
    "question": "NSAIDs mainly work by inhibiting:",
    "options": [
        "A) ACE enzyme",
        "B) COX enzymes",
        "C) MAO enzyme",
        "D) PDE5 enzyme"
    ],
    "answer": "B"
},
{
    "question": "Which COX enzyme protects the gastric mucosa?",
    "options": [
        "A) COX-1",
        "B) COX-2",
        "C) COX-3",
        "D) Lipoxygenase"
    ],
    "answer": "A"
},
{
    "question": "Which COX enzyme is mainly induced during inflammation?",
    "options": [
        "A) COX-1",
        "B) COX-2",
        "C) COX-4",
        "D) COX-5"
    ],
    "answer": "B"
},
{
    "question": "Morphine produces analgesia mainly by acting on:",
    "options": [
        "A) Histamine receptors",
        "B) Opioid receptors",
        "C) Dopamine receptors",
        "D) Muscarinic receptors"
    ],
    "answer": "B"
},
{
    "question": "Which of the following is a non-opioid analgesic?",
    "options": [
        "A) Morphine",
        "B) Codeine",
        "C) Aspirin",
        "D) Fentanyl"
    ],
    "answer": "C"
},
{
    "question": "Which NSAID irreversibly inhibits platelet aggregation?",
    "options": [
        "A) Diclofenac",
        "B) Aspirin",
        "C) Ibuprofen",
        "D) Celecoxib"
    ],
    "answer": "B"
},
{
    "question": "Paracetamol has which major effect?",
    "options": [
        "A) Strong anti-inflammatory",
        "B) Analgesic and antipyretic",
        "C) Anticoagulant",
        "D) Antibiotic"
    ],
    "answer": "B"
},
{
    "question": "The prototype opioid agonist is:",
    "options": [
        "A) Ibuprofen",
        "B) Aspirin",
        "C) Morphine",
        "D) Diclofenac"
    ],
    "answer": "C"
},
{
    "question": "Which NSAID is relatively selective for COX-2?",
    "options": [
        "A) Aspirin",
        "B) Ibuprofen",
        "C) Celecoxib",
        "D) Naproxen"
    ],
    "answer": "C"
},
{
    "question": "The major adverse effect of aspirin is:",
    "options": [
        "A) Hepatotoxicity",
        "B) GI bleeding",
        "C) Nephrotic syndrome",
        "D) Hyperglycemia"
    ],
    "answer": "B"
},
{
    "question": "Paracetamol overdose primarily causes:",
    "options": [
        "A) Kidney stones",
        "B) Liver toxicity",
        "C) Lung fibrosis",
        "D) Bone marrow suppression"
    ],
    "answer": "B"
},
{
    "question": "Which drug has strong anti-inflammatory action?",
    "options": [
        "A) Diclofenac",
        "B) Paracetamol",
        "C) Morphine",
        "D) Tramadol"
    ],
    "answer": "A"
},
{
    "question": "Ibuprofen belongs to which drug class?",
    "options": [
        "A) Opioid analgesic",
        "B) NSAID",
        "C) Corticosteroid",
        "D) Local anesthetic"
    ],
    "answer": "B"
},
{
    "question": "Celecoxib has a lower risk of:",
    "options": [
        "A) Liver toxicity",
        "B) GI ulceration",
        "C) CNS depression",
        "D) Respiratory depression"
    ],
    "answer": "B"
},
{
    "question": "Which opioid is considered the prototype opioid agonist?",
    "options": [
        "A) Codeine",
        "B) Morphine",
        "C) Tramadol",
        "D) Fentanyl"
    ],
    "answer": "B"
},
{
    "question": "Meloxicam is usually taken once daily because it has:",
    "options": [
        "A) Poor absorption",
        "B) Long half-life",
        "C) Rapid metabolism",
        "D) Short duration"
    ],
    "answer": "B"
},
{
    "question": "NSAIDs reduce pain mainly by decreasing:",
    "options": [
        "A) Histamine",
        "B) Prostaglandins",
        "C) Dopamine",
        "D) Acetylcholine"
    ],
    "answer": "B"
},
{
    "question": "Opioids mainly act in the:",
    "options": [
        "A) Peripheral tissues",
        "B) Skin",
        "C) Central nervous system",
        "D) Kidneys"
    ],
    "answer": "C"
},
{
    "question": "Which drug is commonly used for prevention of thrombosis at low doses?",
    "options": [
        "A) Morphine",
        "B) Aspirin",
        "C) Ibuprofen",
        "D) Celecoxib"
    ],
    "answer": "B"
},
{
    "question": "Low-dose aspirin inhibits the formation of:",
    "options": [
        "A) Leukotrienes",
        "B) Thromboxane A2",
        "C) Histamine",
        "D) Bradykinin"
    ],
    "answer": "B"
},
{
    "question": "Which NSAID is commonly associated with gastric ulceration?",
    "options": [
        "A) Aspirin",
        "B) Celecoxib",
        "C) Meloxicam",
        "D) Paracetamol"
    ],
    "answer": "A"
},
{
    "question": "The antidote for paracetamol overdose is:",
    "options": [
        "A) Naloxone",
        "B) Atropine",
        "C) N-acetylcysteine",
        "D) Vitamin K"
    ],
    "answer": "C"
},
{
    "question": "Which opioid is commonly used for severe pain?",
    "options": [
        "A) Ibuprofen",
        "B) Morphine",
        "C) Aspirin",
        "D) Paracetamol"
    ],
    "answer": "B"
},
{
    "question": "Which NSAID has analgesic, antipyretic, and anti-inflammatory effects?",
    "options": [
        "A) Ibuprofen",
        "B) Morphine",
        "C) Fentanyl",
        "D) Codeine"
    ],
    "answer": "A"
},
{
    "question": "Which of the following is an opioid analgesic?",
    "options": [
        "A) Diclofenac",
        "B) Celecoxib",
        "C) Morphine",
        "D) Meloxicam"
    ],
    "answer": "C"
},
{
    "question": "NSAIDs relieve pain primarily by inhibiting the synthesis of:",
    "options": [
        "A) Histamine",
        "B) Prostaglandins",
        "C) Serotonin",
        "D) Acetylcholine"
    ],
    "answer": "B"
},
{
    "question": "Which drug has analgesic and antipyretic effects with minimal anti-inflammatory action?",
    "options": [
        "A) Aspirin",
        "B) Diclofenac",
        "C) Paracetamol",
        "D) Naproxen"
    ],
    "answer": "C"
},
{
    "question": "Morphine mainly produces analgesia by activating:",
    "options": [
        "A) Beta receptors",
        "B) Alpha receptors",
        "C) Opioid receptors",
        "D) Muscarinic receptors"
    ],
    "answer": "C"
},
{
    "question": "Which of the following is a pharmacological action of NSAIDs?",
    "options": [
        "A. Sedation",
        "B. Analgesic action",
        "C. Muscle relaxation",
        "D. Anticoagulation"
    ],
    "answer": "B"
},
{
    "question": "NSAIDs reduce fever by acting on the:",
    "options": [
        "A. Cerebellum",
        "B. Medulla oblongata",
        "C. Hypothalamus",
        "D. Cerebral cortex"
    ],
    "answer": "C"
},
{
    "question": "Which enzyme is inhibited by NSAIDs?",
    "options": [
        "A. Lipoxygenase",
        "B. Phospholipase A2",
        "C. Cyclooxygenase (COX)",
        "D. Acetylcholinesterase"
    ],
    "answer": "C"
},
{
    "question": "Which mediator is primarily decreased by NSAIDs?",
    "options": [
        "A. Dopamine",
        "B. Histamine",
        "C. Prostaglandins",
        "D. Acetylcholine"
    ],
    "answer": "C"
},
{
    "question": "COX-2 is mainly responsible for:",
    "options": [
        "A. Gastric protection",
        "B. Platelet aggregation",
        "C. Pain, fever, and inflammation",
        "D. Renal blood flow"
    ],
    "answer": "C"
},
{
    "question": "Which drug belongs to the salicylates group?",
    "options": [
        "A. Diclofenac",
        "B. Ibuprofen",
        "C. Aspirin",
        "D. Celecoxib"
    ],
    "answer": "C"
},
{
    "question": "Which drug is classified as a propionic acid derivative?",
    "options": [
        "A. Aspirin",
        "B. Ibuprofen",
        "C. Celecoxib",
        "D. Paracetamol"
    ],
    "answer": "B"
},
{
    "question": "Which drug is a COX-2 selective inhibitor?",
    "options": [
        "A. Diclofenac",
        "B. Aspirin",
        "C. Celecoxib",
        "D. Naproxen"
    ],
    "answer": "C"
},
{
    "question": "Which of the following is an opioid analgesic?",
    "options": [
        "A. Aspirin",
        "B. Diclofenac",
        "C. Morphine",
        "D. Ibuprofen"
    ],
    "answer": "C"
},
{
    "question": "Which NSAID action is related to lowering body temperature?",
    "options": [
        "A. Anti-inflammatory",
        "B. Analgesic",
        "C. Antipyretic",
        "D. Antiplatelet"
    ],
    "answer": "C"
},




async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🩺 Welcome to Faris Nursing Bot\n\n"
        "📚 Pharmacology - Chapter 4\n\n"
        "Type /quiz to start the MCQ quiz."
    )

async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["q"] = 0
    context.user_data["score"] = 0
    await send_question(update.message.reply_text, context)


async def send_question(send_func, context):
    q = questions[context.user_data["q"]]

    keyboard = [
        [InlineKeyboardButton(q["options"][0], callback_data="A")],
        [InlineKeyboardButton(q["options"][1], callback_data="B")],
        [InlineKeyboardButton(q["options"][2], callback_data="C")],
        [InlineKeyboardButton(q["options"][3], callback_data="D")]
    ]

    await send_func(
        f"Question {context.user_data['q']+1}/{len(questions)}\n\n{q['question']}",
        reply_markup=InlineKeyboardMarkup(keyboard)

    )
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    current = context.user_data["q"]
    q = questions[current]
    correct = q["answer"]

    if query.data == correct:
        context.user_data["score"] += 1
        await query.edit_message_text(
            f"✅ Correct!\n\nCorrect answer: {q['options'][ord(correct)-65]}"
        )
    else:
        await query.edit_message_text(
            f"❌ Incorrect!\n\nCorrect answer: {q['options'][ord(correct)-65]}"
        )

    await asyncio.sleep(2)

    context.user_data["q"] += 1

    if context.user_data["q"] >= len(questions):
        await query.edit_message_text(
            f"🎉 Quiz Finished!\n\nScore: {context.user_data['score']}/{len(questions)}"
        )
        return

    q = questions[context.user_data["q"]]

    keyboard = [
        [InlineKeyboardButton(q["options"][0], callback_data="A")],
        [InlineKeyboardButton(q["options"][1], callback_data="B")],
        [InlineKeyboardButton(q["options"][2], callback_data="C")],
        [InlineKeyboardButton(q["options"][3], callback_data="D")]
    ]

    await query.edit_message_text(
        f"Question {context.user_data['q']+1}/{len(questions)}\n\n{q['question']}",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("quiz", quiz))
app.add_handler(CallbackQueryHandler(button))
print("Bot is running...")

app.run_polling()