<template>
    <div class="tasks_container">
        <div class="title_tasks_container_block">
            <h1>Articles</h1>
        </div>
        <div class="wrapper_block">
            <div class="main_info_tasks_container_block">
                <p>As World Women's Rights Day approaches, we've put together a selection of seven articles that tell the stories of beautiful ladies.</p>
                <p>As you know, girls are different: strong and selfless, heroic and brave, unhappy or completely out of line with accepted stereotypes.  Read about all of them in this collection.</p>
            </div>

            <div class="articles_block_tasks_container">
                <img src="@/images/IMG_7944.png" alt="">
            </div>

            <div class="main_info_tasks_container_block">
                <p>
                    1. Since this day is dedicated primarily to the struggle for women's rights, let's start with an extremely life-affirming article about a prostitute Leyla from Iraq, who took the protection of women in trouble into her own hands.  This article is about how an ordinary girl from a large family faced the horrors of sexual slavery and why she has to face it with little or no help.
                </p>
            </div>

            <div class="display_flex_main_info_tasks">
                <img src="@/images/IMG_7949.png" alt="">
                <p>2. “Horses die from work, but I am an immortal Moroccan woman, who, however, is not alien to the craving for thanatos.”  A colorful story about how women in Morocco earn their living and why they are forced to work so hard that not every man could stand it.</p>
            </div>

            <div class="main_info_tasks_container_block">
                <p>
                    3. In this article, you will learn why an ordinary woman in Chile adopts dead children.  And no, she doesn't dress them up in doll clothes or have tea parties with imaginary friends.  A touching story about the confrontation between bureaucracy and humanity
                </p>
            </div>

            <div class="diff_img_main_info_tasks">
                <img src="@/images/IMG_7950.png" alt="">
            </div>

        </div>
    </div>
</template>

<script>

export default {
    name: "Articles-Page",
    data() {
        return {
            // tasks
            tasks: ['']
        }
    },
    methods: {
        $http: undefined,
        async getData() {
            try {
                // fetch tasks
                const response = await this.$http.get('http://localhost:8000/api/article');
                // set the data returned as tasks
                this.tasks = response.data;
            } catch (error) {
                // log the error
                console.log(error);
            }
        },
    },
    created() {
        // Fetch tasks on page load
        this.getData();
    }
}
</script>

<style scoped>
    .title_tasks_container_block {
        text-align: center;
    }

    .title_tasks_container_block h1 {
        font-family: 'Linden Hill',serif;
        font-weight: 400;
        font-size: 60px;
        line-height: 81px;

        color: #094067;
    }

    .wrapper_block {
        padding: 0 150px;
    }

    .main_info_tasks_container_block p {
        margin-top: 30px;
        font-family: 'Linden Hill',serif;
        font-style: normal;
        font-weight: 400;
        font-size: 24px;
        line-height: 38px;

        color: #000000;
    }

    .articles_block_tasks_container {
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
    }

    .articles_block_tasks_container img {
        width: 600px;
        height: 400px;
        margin: 75px 0;
    }

    .display_flex_main_info_tasks {
        margin: 75px 0;
        display: flex;
    }

    .display_flex_main_info_tasks img {
        width: 500px;
        height: 500px;
    }

    .display_flex_main_info_tasks p {
        margin-left: 100px;
        font-family: 'Linden Hill',serif;
        font-style: normal;
        font-weight: 400;
        font-size: 24px;
        line-height: 38px;

        color: #000000;
    }

    .diff_img_main_info_tasks {
        text-align: center;
        margin-top: 50px;
        padding-bottom: 100px;
    }

</style>