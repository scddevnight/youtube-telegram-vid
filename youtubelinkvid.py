import telebot
from pytube import Search

# токен бота
BOT_TOKEN = " "

bot = telebot.TeleBot(BOT_TOKEN)

# инлайн запросы
@bot.inline_handler(func=lambda query: query.query)
def inline_query_handler(query):
    query_text = query.query

    # поиск
    search = Search(query_text)
    results = []
    for i in range(5):  # Ищем 5 результатов
        try:
            video = search.results[i]
            results.append(telebot.types.InlineQueryResultArticle(
                id=str(i),  # Идентификатор результата
                title=video.title,
                input_message_content=telebot.types.InputTextMessageContent(
                    f"🎧 {video.title}\n\n[Ссылка на видео](https://www.youtube.com/watch?v={video.watch_url.split('=')[1]})",
                    parse_mode="Markdown"
                )
            ))
        except IndexError:

            pass


    bot.answer_inline_query(query.id, results)


bot.polling(none_stop=True)