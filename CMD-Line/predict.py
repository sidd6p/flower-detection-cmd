import json
import utils as utils 



def main():
    args = utils.input_utils.get_predict_args()

    top_k = args.top_k
    category_names = args.category_names
    gpu = False if args.gpu is None else True
    checkpoint = args.checkpoint
    category_names = args.category_names

    model = utils.model_utils.get_loaded_model(checkpoint)
    probs, predict_classes = utils.model_utils.get_prediction(
        model, utils.data_utils.process_image(args.image_path), top_k, gpu
    )

    with open(category_names, "r") as f:
        cat_to_name = json.load(f, strict=False)

        for i in range(top_k):
            print(
                i + 1,
                " Probability:", probs[i],
                " Predicted Class:", predict_classes[i],
                " Predicted Class name: ", cat_to_name[predict_classes[i]],
            )


if __name__ == "__main__":
    main()
